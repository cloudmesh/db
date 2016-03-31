from ..CloudmeshDatabase import CloudmeshDatabase, CloudmeshMixin
from sqlalchemy import Column, Date, Integer, String


# noinspection PyPep8Naming
class VM_LIBCLOUD(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "vm_libcloud"
    category = "libcloud"
    kind = 'vm'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None, user=None):
        # super(VM_LIBCLOUD, self).set_defaults(name=name, user=user)

        self.user = user or CloudmeshDatabase.user
        self.name = name
        self.label = name

# noinspection PyPep8Naming
class IMAGE_LIBCLOUD(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "image_libcloud"
    category = "libcloud"
    kind = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None, user=None):
        # super(IMAGE_LIBCLOUD, self).set_defaults(name=name, user=user)


        self.user = user or CloudmeshDatabase.user
        self.name = name
        self.label = name