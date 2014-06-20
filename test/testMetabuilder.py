import PyMetabuilder as m


class Kite:
    pass


class KiteBuilder(m.MetaBuilder):
    def __init__(self):
        m.MetaBuilder.__init__(self)
        self.define_kite()

    def define_kite(self):
        #define the model klass to get instances from
        self.model(Kite)
        self.property("design", one_of=["Indoor", "Water Kite", "Kythoon"])
        self.property("line_material", type=str)
        self.property("StringLength", type=int)


builder = KiteBuilder()
builder.design = "kekee"
builder.build()