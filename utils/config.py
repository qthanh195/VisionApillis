import json

file_path = "./utils/config.json"

def load_config():
    global thresh_bg, thresh_pp, ratio, topEdgeDistance, sideEdgeDistance, tolerance
    print("Loading config...")
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        data_config = config['data_config'][0]
        
        
        thresh_bg = data_config['thresh_bg']
        thresh_pp = data_config['thresh_pp']
        ratio = data_config['ratio']
        topEdgeDistance = data_config['topEdgeDistance']
        sideEdgeDistance = data_config['sideEdgeDistance']
        tolerance = data_config['tolerance']
        
        print("Config loaded successfully.")
    except Exception as e:
        print(f"Error loading config: {e}")

def save_config(config):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)

load_config()
