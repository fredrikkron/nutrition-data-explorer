with stg_livsmedel as (select * from {{ source('staging', 'data_Livsmedelsverket') }})

select
    *
from
    stg_livsmedel