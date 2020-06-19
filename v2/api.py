
from versioning import version
blueprint,api=version("v2")
from v2.restaurants import routes
from v2.visitors import routes