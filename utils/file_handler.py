import pickle


class PickleHandler:
    def save_object(self, path, obj):
        with open(path, 'wb') as handle:
            pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_object(self, path):
        with open(path, 'rb') as handle:
            return pickle.load(handle)

    def dumps(self, obj):
        byte_obj = pickle.dumps(obj)
        return byte_obj
