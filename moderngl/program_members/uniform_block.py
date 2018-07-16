__all__ = ['UniformBlock']


class UniformBlock:
    '''
        UniformBlock
    '''

    __slots__ = ['mglo', '_index', '_size', '_name', 'extra']

    def __init__(self):
        self.mglo = None
        self._index = None
        self._size = None
        self._name = None
        self.extra = None
        raise TypeError()

    def __repr__(self):
        return '<UniformBlock: %d>' % self._index

    @property
    def binding(self) -> int:
        '''
            int: The binding of the uniform block.
        '''

        return self.mglo.binding

    @binding.setter
    def binding(self, binding):
        self.mglo.binding = binding

    @property
    def name(self) -> str:
        '''
            str: The name of the uniform block.
        '''

        return self._name

    @property
    def index(self) -> int:
        '''
            int: The index of the uniform block.
        '''

        return self._index

    @property
    def size(self) -> int:
        '''
            int: The size of the uniform block.
        '''

        return self._size
