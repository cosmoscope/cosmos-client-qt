from ..interfaces.decorators import reversible_operation


@reversible_operation
def load_data(path):
    print("Loaded data at ", path)


@load_data.register_undo
def unload_data(path):
    print("Unloaded data at ", path)