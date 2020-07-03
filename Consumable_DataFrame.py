import pandas as pd

data = {'Chips':pd.Series(['Simba', 'Lays'], index =[1,2]),
        'Cooldrink':pd.Series(['Coke', 'Fanta'], index = [1,2]), 
        'Chocolate':pd.Series(['Cadbury','Tex'], index = [1,2]), 
        'Pies':pd.Series(['Pepper Steak', 'Chicken'], index = [1,2]), 
        'Fruit':pd.Series(['Pear','Apple', 'Orange'], index = [1,2,3]), 
        'Cupcakes': pd.Series(['Vanilla', 'Chocolate'], index = [1,2]), 
        'Veggies': pd.Series(['Spinach','Cabbage'], index = [1,2])}

df = pd.DataFrame(data)
print(df)
