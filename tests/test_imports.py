def test_imports():
    """
    I have restuctured these files as a package, and the test
    functions are now outside the package source folder.  This is to
    check that the imports work.
    """
    from whispy import extract
    from whispy import moments
    from whispy import sky
    from whispy import masktool

    # Check that a random function is where it should be
    assert "find_moments" in dir(moments)
