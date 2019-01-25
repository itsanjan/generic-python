import P06_CharCount


    
def test_count():
    input_string = "lll"
    loader = importlib.machinery.SourceFileLoader('P06_CharCount', '/P06_CharCount')
    spec = importlib.util.spec_from_loader(loader.name, loader)
    P06_CharCount = importlib.util.module_from_spec(spec)
    loader.exec_module(P06_CharCount)
    # this is only a stub, to show an example of calling the master_disaster function
    assert P06_CharCount.count_character(input_string) == "l 3"