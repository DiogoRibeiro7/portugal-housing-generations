"""Reproducible descriptive assessment of Portugal's housing market, 2008–2025.

Pipelines (each writes its outputs to ``results/``):

- ``housing_pt.national``: national prices, incomes, housing conditions, construction and financing;
- ``housing_pt.regional``: regional supply panel (NUTS 2024);
- ``housing_pt.affordability``: regional price-to-income affordability;
- ``housing_pt.rental``: rents, tenure and housing-cost burden;
- ``housing_pt.integrated``: the integrated municipal assessment.

``housing_pt.core`` holds parsers, geography, indices and the panel estimators; ``housing_pt.sources`` the
download scripts and the data inventory; ``housing_pt.figures`` the figure scripts. Everything except the figures
uses the standard library only.
"""

__version__ = "1.0.0"
