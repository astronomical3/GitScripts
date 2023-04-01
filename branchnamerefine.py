#Used for removing spaces and stars for each line in the git branch list in qreb (quick rebase).

import os
import sys

print(sys.argv[1].replace("*", "").replace(" ", ""))