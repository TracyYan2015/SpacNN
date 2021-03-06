from module.ModulesFile import ModulesFile, ModelType
from compiler.PRISMParser import ModelConstructor
from model.ModuleFactory import ModuleFactory
from config.SPSConfig import SPSConfig
from PathHelper import get_proj_dir, get_sep


class ModelFactory(object):
    module_factory = ModuleFactory(SPSConfig())

    @classmethod
    def get_built(cls):
        def failurecondition(vs, cs):
            result = vs['sb_status'] == 0 or vs['s3r_status'] == 0 or vs["bcr_status"] == 0 or vs["bdr_status"] == 0
            return result

        def upcondition(vs, cs):
            return not failurecondition(vs, cs)
        labels = {}
        labels['failure'] = failurecondition
        labels['up'] = upcondition
        
        model = ModulesFile(
            ModelType.DTMC,
            failureCondition=failurecondition,
            stopCondition=failurecondition,
            modules=[
                cls.module_factory.timermodule(),
                cls.module_factory.s3rmodule(),
                cls.module_factory.sbmodule(),
                cls.module_factory.bcrmodule(),
                cls.module_factory.bdrmodule()],
            labels=labels)
        model.constants['SCREEN_THICKNESS'] = cls.module_factory.config.getParam('SCREEN_THICKNESS')
        return model

    @staticmethod
    def get_parsed():
        sep = get_sep()
        mdl_dir = sep.join((get_proj_dir(), 'prism_model', 'smalltest.prism'))
        return ModelConstructor().parseModelFile(mdl_dir)

