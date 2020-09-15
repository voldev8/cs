
class HashMap:
    ''' Hash map: A key-value store that uses an array and a hashing function to save and retrieve values.
        Key: The identifier given to a value for later retrieval.'''

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        '''function that takes some input and returns a number.'''
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        '''function that transforms its inputs into some smaller range of possible outputs.'''
        return hash_code % self.array_size

    def assign(self, key, value):
        '''Recipe for saving to a hash table:
            Take the key and plug it into the hash function, getting the hash code.
            Modulo that hash code by the length of the underlying array, getting an array index.
            Check if the array at that index is empty, if so, save the value (and the key) there.
            If the array is full at that index continue to the next possible position depending on your collision strategy.
        '''
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        # to avoid overwriting the wrong key, check the existing value in the array at self.array[array_index]
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # else if collision
        number_collisions = 1
        # Open Addressing: is another way =>finding another value for our hashkey
        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

    def retrieve(self, key):
        '''Recipe for retrieving from a hash table:
            Take the key and plug it into the hash function, getting the hash code.
            Modulo that hash code by the length of the underlying array, getting an array index.
            Check if the array at that index has contents, if so, check the key saved there.
            If the key matches the one you're looking for, return the value.
            If the keys don't match, continue to the next position depending on your collision strategy.
        '''
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return


hash_map = HashMap(3)
hash_map.assign('Darth Vader', 'Star Wars')
hash_map.assign('Captain Kirk', 'Star Trek')
hash_map.assign('Roger Murtaugh', 'Lethal Weapon')

print(hash_map.retrieve("Darth Vader"))
print(hash_map.retrieve("Captain Kirk"))
print(hash_map.retrieve("Roger Murtaugh"))
