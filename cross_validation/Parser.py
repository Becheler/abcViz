
import model
import CrossValidation

class Parser:

    def __to_param(self, dictionary):
        keys = []
        values = []
        for key, val in dictionary.items() :
            keys.append(key)
            values.append(val)
        return model.Param(keys, values)

    def __to_posterior(self, json_params):
        return [ self.__to_param(x) for x in json_params]

    def __make_posteriors(self, dictionary):
        posteriors = []
        for key, value in dictionary.items():
            posteriors.append(self.__to_posterior(value))
        return posteriors

    def build_cross_validation(self, json_object, non_dirac, true_param, plot_names):
        cv = CrossValidation.CrossValidation(non_dirac, true_param, plot_names)
        for posterior in self.__make_posteriors(json_object):
            cv.add_accepted(posterior)
        return cv;
