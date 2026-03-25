import unittest

from win32more._generic import Generic, GenericAlias, TypeVar, generic_is_concrete

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class TestGeneric(unittest.TestCase):
    def test_generic_getitem_creates_generic_alias(self):
        self.assertIsInstance(Generic[T], GenericAlias)
        self.assertIs(Generic[T].__origin__, Generic)
        self.assertEqual(Generic[T].__args__, (T,))
        self.assertEqual(Generic[T].__parameters__, (T,))

    def test_parameter_to_generic_must_be_type_variable(self):
        # TypeError: Parameters to Generic[...] must all be type variables or parameter specification variables.
        with self.assertRaises(TypeError):
            Generic[int]

    def test_number_of_arguments_must_be_same_as_parameters(self):
        class A(Generic[T, K]):
            pass

        # TypeError: Too few arguments for <class A>
        with self.assertRaises(TypeError):
            A[T]

        # TypeError: Too many arguments for <class A>
        with self.assertRaises(TypeError):
            A[T, K, V]

    def test_inherit(self):
        class A(Generic[T]):
            pass

        class B(Generic[T]):
            pass

        class C(A[T], B[T]):
            pass

        class D(A[T], int):
            pass

        class E(Generic[T], A[T]):
            pass

        class F(A[B[T]]):
            pass

        self.assertTrue(issubclass(A, Generic))
        self.assertIs(A.__bases__[0], Generic)
        self.assertEqual(C.__bases__, (A, B))
        self.assertEqual(D.__bases__, (A, int))
        self.assertEqual(E.__bases__, (A,))
        self.assertEqual(F.__bases__, (A,))
        self.assertEqual(F.__parameters__, (T,))

        # TypeError: duplicate base class A
        with self.assertRaises(TypeError):

            class G(Generic[K, V], A[K], A[V]):
                pass

    def test_parameters_and_args(self):
        class A(Generic[K, V]):
            pass

        class B(Generic[T, K, V], A[K, V]):
            pass

        self.assertEqual(A.__parameters__, (K, V))
        self.assertEqual(A[int, T].__parameters__, (T,))
        self.assertEqual(A[int, T].__args__, (int, T))
        self.assertEqual(B.__parameters__, (T, K, V))

    def test_concrete(self):
        class Base:
            pass

        class A(Generic[T], Base):
            pass

        class B(A[T]):
            pass

        self.assertNotIsInstance(A[int], GenericAlias)
        self.assertTrue(generic_is_concrete(A[int]))
        self.assertTrue(issubclass(A[int], Base))
        self.assertEqual(A[int].__bases__, (A, Base))
        self.assertEqual(A[int].__name__, "A_int")
        self.assertEqual(A[int].__args__, (int,))
        self.assertEqual(A[int].__parameters__, (T,))
        self.assertIs(A[int], A[int])
        self.assertNotIsInstance(B[int], GenericAlias)
        self.assertTrue(issubclass(B[int], Base))
        self.assertTrue(issubclass(B[int], A[int]))


if __name__ == "__main__":
    unittest.main()
