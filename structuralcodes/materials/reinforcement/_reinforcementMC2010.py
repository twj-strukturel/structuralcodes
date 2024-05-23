"""The concrete class for Model Code 2010 Reinforcement Material."""

import typing as t

from structuralcodes.codes import mc2010

from ._reinforcement import Reinforcement


class ReinforcementMC2010(Reinforcement):
    """Reinforcement implementation for MC 2010."""

    def __init__(
        self,
        fyk: float,
        Es: float,
        ftk: float,
        epsuk: float,
        gamma_s: t.Optional[float] = None,
        name: t.Optional[str] = None,
        density: float = 7850.0,
    ):
        """Initializes a new instance of Reinforcement for MC2010.

        Args:
            fyk (float): Characteristic yield strength in MPa.
            Es (float): The Young's modulus in MPa.
            ftk (float): Characteristic ultimate strength in MPa.
            epsuk (float): The characteristik strain at the ultimate stress
                level.
            gamma_s (Optional(float)): The partial factor for reinforcement.
                Default value is 1.15.

        Keyword Args:
            name (str): A descriptive name for the reinforcement.
            desnsity (float): Density of material in kg/m3 (default: 7850).
        """
        if name is None:
            name = f'Reinforcement{round(fyk):d}'
        super().__init__(
            fyk=fyk,
            Es=Es,
            name=name,
            density=density,
            ftk=ftk,
            epsuk=epsuk,
            gamma_s=gamma_s,
        )

    def fyd(self) -> float:
        """The design yield strength."""
        return mc2010.fyd(self.fyk, self.gamma_s)

    @property
    def gamma_s(self) -> float:
        """The partial factor for reinforcement."""
        return self._gamma_s or 1.15