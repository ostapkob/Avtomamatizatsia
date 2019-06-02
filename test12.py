from collections import Counter, defaultdict
from pprint import pprint

def tenure_bucket(tenure):
    if tenure < 2: return "<2"
    elif tenure < 5: return "<5"
    else: return ">5"

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salaries_by_tenure = defaultdict(list)

for salaris, experience in salaries_and_tenures:
    salaries_by_tenure[experience].append(salaris)



# pprint(salaries_by_tenure)
# avg_salary_by_tenure={}
# for i, j in salaries_by_tenure.items():
#     group = tenure_bucket(i)
#     avg_salary_by_tenure[tenure_bucket(i)] = sum(j)/len(j) 
#     print(i, j, avg_salary_by_tenure )





avg_salary_by_tenure={tenure: sum(salaris)/len(salaris)
                     for tenure, salaris  in salaries_by_tenure.items()
                     }

pprint(avg_salary_by_tenure)
