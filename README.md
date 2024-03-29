# Python Test

Read this page for clear understanding

https://realpython.com/python-mock-library/#common-mocking-problems

## Good Reads
https://stackoverflow.com/questions/18872550/unittest-mock-patch-a-class-instance-and-set-method-return-values

## Where to patch

patch() works by (temporarily) changing the object that a name points to with another one. There can be many names pointing to any individual object, so for patching to work you must ensure that you patch the name used by the system under test.

The basic principle is that you patch where an object is looked up, which is not necessarily the same place as where it is defined. A couple of examples will help to clarify this.

Imagine we have a project that we want to test with the following structure:

```
a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> some_function instantiates SomeClass
```

Now we want to test some_function but we want to mock out SomeClass using patch(). The problem is that when we import module b, which we will have to do then it imports SomeClass from module a. If we use patch() to mock out a.SomeClass then it will have no effect on our test; module b already has a reference to the real SomeClass and it looks like our patching had no effect.

The key is to patch out SomeClass where it is used (or where it is looked up). In this case some_function will actually look up SomeClass in module b, where we have imported it. The patching should look like:

`@patch('b.SomeClass')`


However, consider the alternative scenario where instead of from a import SomeClass module b does import a and some_function uses a.SomeClass. Both of these import forms are common. In this case the class we want to patch is being looked up in the module and so we have to patch a.SomeClass instead:

`@patch('a.SomeClass')`

