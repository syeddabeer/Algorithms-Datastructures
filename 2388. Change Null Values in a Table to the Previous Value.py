import pandas as pd

def change_null_values(coffee_shop: pd.DataFrame) -> pd.DataFrame:
    coffee_shop['drink']=coffee_shop['drink'].fillna(method='ffill')
    return coffee_shop

with cte as (
    select id, drink, row_number() over() as rn
    from CoffeeShop
),

cte2 as (
    select id, drink, rn, sum(if(drink is NULL, 0, 1)) over (order by rn) as group_id
    from cte
)

select id, first_value(drink) over (partition by group_id order by rn) as drink
from cte2


