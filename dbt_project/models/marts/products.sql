-- models/marts/products.sql
select
    -- Convert item_id from text to a number (integer)
    distinct cast(itemid as integer) as item_id
    
from {{ ref('stg_events') }}
where itemid is not null