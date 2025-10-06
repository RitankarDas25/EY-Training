import yaml

config ={
    "model":"random forest",
    "params":{
        "n_estimators":100,
        "max_depth":10,
    },
    "dataset":"students.csv"
}

#write to yaml file
with open("config.yml",'w') as f:
    yaml.dump(config,f)

#read yaml
with open("config.yml",'r') as f:
    data = yaml.safe_load(f)


print(data)