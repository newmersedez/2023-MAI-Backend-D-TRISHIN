from lru_cache import LRUCache

if __name__ == '__main__':
    cache = LRUCache(5)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    print("Output:", cache.get('Jesse'))
    cache.rem('Walter')
    print("Output:", cache.get('Walter'))

    cache.rem('Jesse')

    cache.set('1', 'Hello')
    cache.set('2', 'World')
    cache.set('3', '1337')
    cache.set('4', 'Test')
    cache.set('5', 'Cache')
    print("Output:", cache.get('1'))

    cache.set('6', 'f')
    print("Output:", cache.get('1'))
    print("Output:", cache.get('4'))
    print("Output:", cache.get('2'))
    print("Output:", cache.get('6'))
    print(f"Output: '{cache.get('-1')}'")
