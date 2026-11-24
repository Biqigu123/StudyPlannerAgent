from memory import save_data,load_data
def create_plan(plan):
    plans = load_data("plans.json")
    plans.append(plan)
    save_data("plans.json",plans)

def get_plans():
    return load_data("plans.json")
def save_progress(progress):
    data = load_data("progress.json")
    data.append(progress)
    save_data( "progress.json",data)

def get_progress():
    return load_data("progress.json")