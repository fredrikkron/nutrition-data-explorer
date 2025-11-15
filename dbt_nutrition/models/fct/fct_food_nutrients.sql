with src_livsmedel as (
    select
        s.food_id,
        n.nutrient_id,
        s.value
    from {{ ref('src_livsmedel') }} s
    join {{ ref('dim_nutrients') }} n
        on s.nutrient_name = n.nutrient_name
)

select
    f.food_id,
    s.nutrient_id,
    s.value
from src_livsmedel s
inner join {{ ref('dim_food') }} f
    on s.food_id = f.food_id