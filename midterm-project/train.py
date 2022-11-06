# Import Libraries
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


model_out = 'model.bin'
# import data
df = pd.read_csv('dataset/default-of-credit-card-clients.csv')

# i will remove the id 
del df['ID']

# rename the default payment next month 
df.rename(columns = {'default payment next month':'default_payment'}, inplace = True)

# rename the pay_0 to pay_1
df.rename(columns = {'PAY_0':'PAY_1'}, inplace = True)

# convert columns name  to lowercase
df.columns = df.columns.str.lower()

### Mapping on Categorilca Varieables ###

pay_status = ['pay_1', 'pay_2',
       'pay_3', 'pay_4', 'pay_5', 'pay_6']

for i in pay_status:
    df = df.loc[(df[i] != 0)]


# - add one to payment status to fix 


for i in pay_status:
    df[i] = df[i] + 1

# for sex 
sex_values = {
    1: 'male',
    2: 'female'
}

df.sex = df.sex.map(sex_values)



df['education'] =  df['education'].replace([0, 5, 6], 4)
# now there are just 4 types

education_values = {
    1: 'graduate school',
    2: 'university',
    3: 'high school',
    4: 'other'
}

df.education = df.education.map(education_values)


# ##### For marriage


df['marriage'] =  df['marriage'].replace(0, 3)

marriage_values = {
    1: 'married',
    2: 'single',
    3: 'other'
}

df.marriage = df.marriage.map(marriage_values)

# ### Split the Data


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state= 53)


df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)


# #### Create y
y_train = df_full_train.default_payment.values
y_test = df_test.default_payment.values

del df_full_train['default_payment']
del df_test['default_payment']



full_train_dicts = df_full_train.to_dict(orient='records')
test_dicts = df_test.to_dict(orient='records')

dv = DictVectorizer(sparse=False)

# ##### Create X

X_train =  dv.fit_transform(full_train_dicts)
X_test = dv.transform(test_dicts)

model = RandomForestClassifier(n_estimators=25,max_depth=7,random_state=53)
model.fit(X_train, y_train)


y_pred =  model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred)
score = model.score(X_test, y_test)
print('score = %.3f' % score)
print('auc = %.3f' % auc)


with open(model_out, 'wb') as f_out:
    pickle.dump((dv, model), f_out)


print(f"the model is saved to {model_out} ")
