import blockNames

class DENSITY_CALCULATOR_TYPES:
    null, heaviside, quadratic = range(3)

DENSITY_CALCULATOR_TYPE_TO_STRING_DICTIONARY = {
    DENSITY_CALCULATOR_TYPES.heaviside : blockNames.DensityCalculator.heaviside,
    DENSITY_CALCULATOR_TYPES.null : blockNames.DensityCalculator.null,
    DENSITY_CALCULATOR_TYPES.quadratic: blockNames.DensityCalculator.quadratic
}
