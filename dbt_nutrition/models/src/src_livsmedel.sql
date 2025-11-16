with stg_livsmedel as (select * from {{ source('staging', 'data_Livsmedelsverket') }})

select
    Livsmedelsnummer as food_id,
    Livsmedelsnamn as food_name,
    coalesce(Gruppering, 'Övrigt') as food_group,
    trim(split_part(Näringsämne, ' (', 1)) as nutrient_name,
    trim(replace(replace(split_part(Näringsämne, '(', 2), ')', ''), ' ', '')) as unit,
    Värde as value
from
    stg_livsmedel
where unit NOT IN ('kJ', 'C22:5', 'C20:5', 'C22:6', 'NE/mg', 'skaletc.', 'RE/µg')