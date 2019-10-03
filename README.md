# hex
Hex

Yet another attempt at figuring out visual abstraction for large codebase...

Abstractions : 

- distribution as native concept (see http://users.umiacs.umd.edu/~vishkin/XMT/index.shtml). [NC](https://en.wikipedia.org/wiki/NC_(complexity)) Complexity problems should be simply and directly tractable via data manipulation or compiled code.
Find simplest possible language class for this in https://en.wikipedia.org/wiki/Chomsky_hierarchy 

- Be aware of [Automata Theory](https://en.wikipedia.org/wiki/Automata_theory) and relationships with Finite State Machines, which is a widely understood programming paradigm. For visualization purposes, the translation FSM <-> regular expression is a well known and well studied one. We might want to start from there...

- FSM are inherently synchronous, so they work to express *space* ( local data complexity ) or *time* (locally on one machine) structure. Recall that FSM with memory are equivalent to FSM with recursion (non-acyclic graph) => maybe there is a nugget hidden here about generalizing FSM via distributed memory, maybe non-determinism should be added tho...

- Ultimately target PSPACE problems, are these seems to be the good balance between simple and tractable problems.


Graphics (2D only, potentially as a projection of 3D) :

- [Implicit surfaces](https://en.wikipedia.org/wiki/Implicit_surface) should give us a very simple way to abstract a graphical representation of things...

- [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) or [Minkowski Sum](https://en.wikipedia.org/wiki/Minkowski_addition) should give us a way to visualize combinatorial behavior of things... A categorical take on this would be useful to match with the abstraction they represent...



