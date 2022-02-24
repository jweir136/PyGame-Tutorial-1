The main issue with this version is how it stores nodes. Since nodes are stores as a simple list, in order to do any transformation to a wireframe, you must iterate through all the nodes one by one.
This makes any scene with a large number of nodes too slow to do any operations on.

This can be fixed by using matrices.
