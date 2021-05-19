import pandas as pd


def main():
    list_effectiveness = import_effectiveness()
    list_types = get_types(list_effectiveness)
    li = find_n_way_double(list_effectiveness, list_types, 16)
    for row in li:
        print(row)
    print(len(li))


def import_effectiveness():
    path = 'effectiveness.csv'
    df = pd.read_csv(path, index_col=0)
    return df


def get_types(df):
    list_types = df['Attacking'].drop_duplicates()
    return list_types.tolist()


def find_n_way_double(list_effectiveness, list_types, n):
    li = []
    list_types = ['Bug']
    for t in list_types:
        df = list_effectiveness.loc[list_effectiveness['Attacking'] == t]
        res = super_effective(list_effectiveness, t, n, df, 1, [])
        if type(res) is str:
            li.append([res, t])
        if type(res) is list:
            if len(res) == 0:
                continue
            ali = []
            for row in res:
                ali.append(row + [t])
            li = li + ali
    return li


def super_effective(list_effectiveness, t, n, df, i, li_def0):
    li = []
    for index, row in df.iterrows():
        attacking = row['Attacking']
        defending = row['Defending']
        effectiveness = row['Effectiveness']
        if effectiveness == 'Super effective':
            mask = list_effectiveness['Attacking'] == defending
            li_def1 = li_def0 + [defending]
            for defender in li_def1:
                mask1 = list_effectiveness['Defending'] != defender
                mask = mask1 & mask
            df = list_effectiveness.loc[mask]



            if defending == t and i == n:
                print(li_def0)
                return attacking
            if i < n:
                res = super_effective(list_effectiveness, t, n, df, i + 1, li_def1)
                if type(res) is str:
                    li.append([attacking, res])
                if type(res) is list:
                    if len(res) == 0:
                        continue
                    ali = []
                    for row in res:
                        ali.append([attacking] + row)
                    li = li + ali
    return li


if __name__ == '__main__':
    main()
