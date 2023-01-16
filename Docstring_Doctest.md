# Docstring y Doctest

## 1) Comentarios

```py
# Nos permite comentar una sola línea

"""
Este comentario posee
saltos de línea
'''
hola
'''
"""

'''
Este comentario
también posee
saltos de línea
"""
sasdasd
"""
'''
```

## 2) Docstring

```py
# Docstring

def palindromo(sentence: str) -> bool:
    """
    Permite conocer si un string es, o no, un palíndromo.

    Args:
        sentence: string

    Returns:
        bool
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
```

## 3) Formato de docstring

```py
# Docstring

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, un palíndromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
```

## 4) Doctest

```py
# Docstring

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, un palíndromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False

    Examples:
        >>> palindromo('anita lava la tina')
        True

        >>> palindromo('CodigoFacilito')
        False

        >>> sentence = 'Oso'
        >>> palindromo(sentence)
        True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


# python3 -m doctest 4-doctest.py
# python3 -m doctest 4-doctest.py -v
```

## 5) Objetos documentales

```py
"""Este es el Docstring del módulo 5_objetos_documentales.py"""
# Docstring

class User:
    """Permite representar un usuario."""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo User

        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña.
        """


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, un palíndromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False

    Examples:
        >>> palindromo('anita lava la tina')
        True

        >>> palindromo('CodigoFacilito')
        False

        >>> sentence = 'Oso'
        >>> palindromo(sentence)
        True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


# python3 -m doctest 4-doctest.py
# python3 -m doctest 4-doctest.py -v
```

## 6) Pruebas con archivos externos

```py
"""Este es el Docstring del módulo main.py"""
# Docstring

class User:
    """Permite representar un usuario."""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo User

        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña.
        """

        self.username = username
        self.password = password


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, un palíndromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


# python3 -m doctest 4-doctest.py
# python3 -m doctest 4-doctest.py -v

# python3 -m doctest test_6-pruebas-archivos-ext.txt
```

```
>>> from main import palindromo, User

>>> palindromo('anita lava la tina')
True

>>> palindromo('CodigoFacilito')
False

>>> sentence = 'Oso'
>>> palindromo(sentence)
True

>>> user = User('eduardo', '123strong')

>>> user.username = 'eduardo'
True

>>> user.password = '123sarasa'
False
```
