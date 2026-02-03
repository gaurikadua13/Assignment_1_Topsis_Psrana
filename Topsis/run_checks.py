from topsis_gaurika_dua_10203271.core import run_topsis
import pandas as pd

# create input
pd.DataFrame({'Name':['A','B','C'],'C1':[1,2,3],'C2':[4,5,6],'C3':[7,8,9]}).to_csv('tmp_in.csv',index=False)
# run
run_topsis('tmp_in.csv','1,1,1','+,+,+','tmp_out.csv')
# show
print('WROTE tmp_out.csv')
print(pd.read_csv('tmp_out.csv').columns.tolist())
print(pd.read_csv('tmp_out.csv'))
