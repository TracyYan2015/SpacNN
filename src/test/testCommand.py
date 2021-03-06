from compiler.PRISMParser import ModelConstructor as Constructor


def buildCommand():
    constructor = Constructor()
    model = constructor.parseModelFile("../../prism_model/CommandTest.prism")
    return model.modules.values()[0].commands.values()[0]


def test():
    cmd = buildCommand()
    assert cmd.evalGuard() == True
    cmd.execAction()
    assert cmd.vs['a'].getValue() == 0


if __name__ == '__main__':
    test()
