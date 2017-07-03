# DES modeling for the pyroprocessing system

**Discrete event simulation description**
<br>In DES, each 'event' is a 'vertex.'
<br>There are state changes and/or parameters associated with a vertex.
<br>State changes are assigning values to a variable or solving an equation.
<br>Parameters are variables needed to make the state change.
<br>DES steps discretely in time through each vertex via an 'edge.'
<br>At each vertex, the equations are run and the state variables change.
<br>The edges are dynamic and provide logical relationships between events.
<br>DES should readily lend itself to the modeling of batch systems like pyroprocessing.
<br>Python is a natural fit for DES due to its modularity.
