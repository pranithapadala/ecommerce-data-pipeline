-- models/marts/users.sql
select
    -- Convert visitorid from text to a number (integer)
    distinct cast(visitorid as integer) as visitor_id

from {{ ref('stg_events') }}