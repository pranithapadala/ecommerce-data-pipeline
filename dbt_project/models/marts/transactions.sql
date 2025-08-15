-- models/marts/transactions.sql

with source_data as (
    select * from {{ ref('stg_events') }}
)
select
    -- 1. Fix the data type for transaction_id
    cast(transactionid as integer) as transaction_id,
    
    -- We will find the first timestamp for the transaction
    min(to_timestamp(timestamp / 1000)) as transaction_timestamp,
    
    -- 2. Fix the data type for visitor_id to match the users table
    cast(min(visitorid) as integer) as visitor_id,
    
    -- Let's count how many items were in this transaction
    count(itemid) as number_of_items
    
from source_data
where event = 'transaction' and nullif(transactionid, '') is not null

group by 
    transactionid