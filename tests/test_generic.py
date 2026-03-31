import unittest
from typing import Generic, _GenericAlias

from win32more._win32 import ComPtr, Int16, Int32, Int64
from win32more._winrt import K, T, V


class TestGeneric(unittest.TestCase):
    def test_generic_getitem_creates_generic_alias(self):
        class A(Generic[T], ComPtr):
            pass

        self.assertIsInstance(A[K], _GenericAlias)
        self.assertIs(A[K], A[K])
        self.assertEqual(A[K].__args__, (K,))
        self.assertEqual(A[K].__parameters__, (K,))

        class B(Generic[K, V], ComPtr):
            pass

        self.assertIsInstance(B[T, Int32], _GenericAlias)
        self.assertIs(B[T, Int32], B[T, Int32])
        self.assertEqual(B[T, Int32].__args__, (T, Int32))
        self.assertEqual(B[T, Int32].__parameters__, (T,))

    def test_generic_getitem_creates_concrete_class(self):
        class A(Generic[T], ComPtr):
            pass

        self.assertIsInstance(A[Int32], type)
        self.assertIs(A[Int32], A[Int32])
        self.assertEqual(A[Int32].__bases__, (A, ComPtr))
        self.assertEqual(A[Int32].__args__, (Int32,))

        class B(A[Int32], Generic[K, V]):
            pass

        self.assertIs(B[Int16, Int64], B[Int16, Int64])
        self.assertEqual(B[Int16, Int64].__bases__, (B, A[Int32]))
        self.assertEqual(B[Int16, Int64].__args__, (Int16, Int64))
        self.assertEqual(B[Int16, Int64]._B__args, (Int16, Int64))
        self.assertEqual(B[Int16, Int64]._A__args, (Int32,))


if __name__ == "__main__":
    unittest.main()
