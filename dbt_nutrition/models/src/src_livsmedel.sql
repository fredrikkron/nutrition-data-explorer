with stg_livsmedel as (select * from {{ source('staging', 'data_Livsmedelsverket') }})

select
    Livsmedelsnummer as food_id,
    Livsmedelsnamn as food_name,
    Gruppering as food_group,
    trim(split_part(Näringsämne, ' (', 1)) as nutrient_name,
    trim(replace(replace(split_part(Näringsämne, '(', 2), ')', ''), ' ', '')) as unit,
    Värde as value
from
    stg_livsmedel
where unit != 'kJ'