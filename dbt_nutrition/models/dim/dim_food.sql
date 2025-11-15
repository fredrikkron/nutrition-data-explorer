with src_livsmedel as (
    select
        food_id,
        food_name,
        food_group
    from {{ ref('src_livsmedel') }}
)

select
    distinct food_id,
    food_name,
    food_group
from
    src_livsmedel
order by
    food_id