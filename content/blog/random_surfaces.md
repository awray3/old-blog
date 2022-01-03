Title: Random Surfaces
Date: 2022-01-01
Summary: Meandering through the world of random surfaces.
Status: draft

# Random Surfaces

Random surfaces lie at the intersection of many interesting areas of study: probability,
geometry, functional analysis, and an area of theoretical physics known as
_Liouville Quantum Gravity_. 
If you're interested in starting to dig into this subject, here are some places to start,
at various levels of technicality:

* This [Quanta article](https://www.quantamagazine.org/mathematicians-prove-2d-version-of-quantum-gravity-really-works-20210617/)
is how I first found out about this subject.
* This [expository arXiv paper](https://arxiv.org/abs/1908.05573) by Ewain Gwynne is a
wonderful tour through the core of the subject of random surfaces at a bird's-eye view,
and it contains references to papers and texts which go into more detail.
* This series of three groundbreaking papers[^1], which are the subject of the article above:
	1. [Liouville Quantum Gravity on the Riemann sphere](https://arxiv.org/abs/1410.7318), 2014
	2. [Integrability of Liouville theory: proof of the DOZZ Formula](https://arxiv.org/abs/1707.08785), 2017
	3. [Conformal bootstrap in Liouville Theory](https://arxiv.org/abs/2005.11530), 2020



One interesting thing about these papers is they give a mathematically-sound
construction of the Feynmann path integral in a 2D quantum field theory known as _Liouville Field Theory_.
The original physics covered in these papers was carried out in the early 80's,
but the novel thing is that this could be made mathematically rigorous. The Feynmann path
integral has always been a mythical thing to mathematicians, and there have been numerous
attempts at making it rigorous, though none seem to do it justice. (There could probably be a whole post just on those!)

In reading through these sources I learned about the idea of a _random surface_, which is the topic of this post. To explain,
I'll follow Gwynne and first discuss what a _random curve_ is.

# Random Curves

Let's start with thinking about random curves. What makes a curve "random?" What do we even mean by curve?
There are a lot of questions to make sense of here. Let's start with a nice looking curve:

[nice looking picture of curve here]

One option is to take every point on that curve and wiggle it "randomly." You might expect it look sort-of like
this:

[Same curve with some noise added to it]

You might describe this as a "noisy smooth curve." 

Mathematically, a random curve can be constructed as a limit of random walks in the lattice
$ℤ^d ⊂ ℝ^d$, so let's start by describing that.



<!-- It is unexpected that the Gaussian Free Field even exists. It's a random variable valued in the space $H^1(D)$ where $D \subset \mathbb{C}$ -->
<!-- is the unit disk in the complex plane, and $H^1$ is the space of _Sobolev functions_. More -->
<!-- on them later. -->



[^1]: I have not read the last three papers in any detail; though they are fun to glance through to get a feel for the work they did.