# Build a json file to configure SchNetPack.
import os
import sys
import json
import argparse
from experiment_setup import current_setup, str_to_bool
# %%
# parser = argparse.ArgumentParser(
#     description="Semi-Supervised ML for Synthesizability Prediction"
# )
# parser.add_argument(
#     "--experiment",
#     default="alignn0",
#     help="name of the experiment and corresponding config files.",
# )
# parser.add_argument(
#     "--ehull",
#     type=str_to_bool,
#     default=False,
#     help="Predicting stability to evaluate PU Learning's efficacy.",
# )
# parser.add_argument(
#     "--ehull015",
#     type=str_to_bool,
#     default=False,
#     help="Predicting stability to evaluate PU Learning's efficacy with 0.015eV cutoff.",
# )
# parser.add_argument(
#     "--small_data",
#     type=str_to_bool,
#     default=False,
#     help="This option selects a small subset of data for checking the workflow faster.",
# )
# args = parser.parse_args(sys.argv[1:])
# experiment = args.experiment 
# ehull_test = args.ehull
# ehull015 = args.ehull015
# small_data = args.small_data
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(current_dir,'../../'))
# os.chdir("alignn/alignn_configs")
def alignn_pu_config_generator(experiment, small_data, ehull_test, ehull015):
    cs = current_setup(ehull_test=ehull_test, small_data=small_data, experiment=experiment, ehull015=ehull015)
    # propDFpath = cs["propDFpath"]
    # result_dir = cs["result_dir"]
    prop = cs["prop"]
    # TARGET = cs["TARGET"]
    data_prefix = cs["dataPrefix"]
    max_num_of_iterations = 60#100
    start_of_iterations = 0  
    data_dir = "data/clean_data"
    root_dir = os.path.join(data_dir,"alignn_format")
    pu_setup = dict()
    alignn_dir = "pu_alignn"
    alignn_config_dir = os.path.join(alignn_dir,"alignn_configs")
    default_class_config = os.path.join(alignn_config_dir, 'default_class_config.json')
    class_config_name = os.path.join(alignn_config_dir, f'class_config_{data_prefix}{experiment}_{prop}.json')
    pu_config_name = os.path.join(alignn_config_dir, f'pu_config_{data_prefix}{experiment}_{prop}.json')
    pu_setup["default_class_config"] =default_class_config
    pu_setup["pu_config_name"] =pu_config_name
    pu_setup["class_config_name"] =class_config_name
    pu_setup["data_dir"]=data_dir
    pu_setup["root_dir"]=root_dir
    pu_setup["file_format"] = "poscar"
    pu_setup["keep_data_order"]=False #overwrites this attrib in config
    pu_setup["classification_threshold"] = 0.5 #also overwrites if present
    pu_setup["batch_size"]=None
    pu_setup["output_dir"] = None
    pu_setup["epochs"]= 120
    pu_setup["max_num_of_iterations"]= max_num_of_iterations
    pu_setup["start_of_iterations"]= start_of_iterations
    pu_setup["small_data"]= small_data
    
    print(os.getcwd())
    with open(pu_setup["pu_config_name"], "w+") as configJson:
        json.dump(pu_setup, configJson, indent=2)

    print(f'New PU Alignn pu_config_{data_prefix}{experiment}_{prop}.json was generated.')
        
    return pu_config_name

# alignn_pu_config_generator(experiment = experiment, 
#                            small_data = small_data,
#                            ehull_test = ehull_test)

# need to update this with experiment_setup.py
# also, don't need the id_prop_dat anymore.

# # Build a json file to configure SchNetPack.
# import os
# import json
# # os.chdir("alignn/alignn_configs")
# # experiment_name = "alignn0"
# # experiment_name = 'coAlSch1'
# experiment_name = 'coAlSch2'
# cotraining = True
# max_num_of_iterations = 99
# start_of_iterations = 1  #default is 1
# data_dir = "data/clean_data"
# root_dir = os.path.join(data_dir,"alignn_format")
# pu_setup = dict()
# alignn_dir = "alignn"
# alignn_config_dir = os.path.join(alignn_dir,"alignn_configs")
# coConfigPath = None
# default_class_config = os.path.join(alignn_config_dir, 'default_class_config.json')
# class_config_name = os.path.join(alignn_config_dir, 'class_config_'+experiment_name+'.json')
# pu_config_name = os.path.join(alignn_config_dir, 'pu_config_'+experiment_name+'.json')
# pu_setup["default_class_config"] =default_class_config
# pu_setup["pu_config_name"] =pu_config_name
# pu_setup["class_config_name"] =class_config_name
# pu_setup["cotraining"] =cotraining
# pu_setup["data_dir"]=data_dir
# pu_setup["root_dir"]=root_dir
# pu_setup["file_format"] = "poscar"
# pu_setup["keep_data_order"]=False #overwrites this attrib in config
# pu_setup["classification_threshold"] = 0.5 #also overwrites if present
# pu_setup["batch_size"]=None
# pu_setup["output_dir"] = None
# pu_setup["epochs"]= None
# pu_setup["max_num_of_iterations"]= max_num_of_iterations
# pu_setup["start_of_iterations"]= start_of_iterations


# with open(pu_setup["pu_config_name"], "w") as configJson:
#     json.dump(pu_setup, configJson, indent=2)