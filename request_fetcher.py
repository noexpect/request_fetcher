import pickle
import os

class RequestFetcher:
    def __init__(self):
        self.position_path="position.dump"
        self.initial_entry = {"position_id":0}
        self.current_state = self.initial_entry

    def restore_state(self):
        if os.path.exists(self.position_path):
            print("pickled file found")
            with open(self.position_path, 'rb') as f:
                previous_state = pickle.load(f)
                if previous_state:
                    print("previous state:", previous_state)
                    self.current_state = previous_state
        else:
            print("previous state not found. So initialized.")
            self._save_state(self.current_state)

    def _save_state(self, state):
        with open(self.position_path, 'wb') as f:
            pickle.dump(state, f)
            print("saved state:", state)
            self.current_state = state

    def fetch(self):
        print("do something with pickled state: ", self.current_state)
        new_postion = self.current_state["position_id"] + 1 # get new state from result of what you do.
        self._save_state({"position_id":new_postion})

if __name__ == '__main__':
    rf = RequestFetcher()
    rf.restore_state()
    rf.fetch()
