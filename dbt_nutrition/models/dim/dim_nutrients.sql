with src_livsmedel as (
    select 
        distinct nutrient_name,
        unit
    from {{ ref('src_livsmedel') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['nutrient_name']) }} as nutrient_id,
    nutrient_name,
    unit
from
    src_livsmedel
order by
    nutrient_id