import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np

sns.set(color_codes=True)

class CrossValidation:

    _ylabel = 'Probability density'
    _title = 'ABC posterior estimation cross-validation'
    _accepted_parameters = []

    def __init__(self, non_dirac, true_param, plot_names):
        self._non_dirac_priors = non_dirac
        self._true_param = true_param
        self._plot_names = plot_names

    def __plot_true_param(self, axes, true_theta):
        axes.vlines(true_theta, ymin= 0, ymax = 1, color='b', lw = 1, linestyle='--')
        return axes;

    def __plot_prior(self, axes, x, pdf):
        y = pdf(x)
        axes.plot(x,y,color='g',lw=1)
        axes.fill_between(x, y, color="g", alpha=0.3)
        return axes;

    def __plot_posterior(self, axes, data):
        axes = sns.kdeplot(data, color="k", lw=1);
        return axes;

    def __decorate(self, axes, param_name):
        axes.set_xlabel(param_name)
        return axes;

    def __plot_parameter(self, axes, support, posteriors, true_theta, prior_pdf, theta_name):
        self.__plot_prior(axes, support, prior_pdf)

        for posterior in posteriors :
            if(len(posterior)) > 30:
                self.__plot_posterior(axes, posterior)

        self.__plot_true_param(axes, true_theta)
        return self.__decorate(axes, theta_name);

    def add_accepted(self, params):
        self._accepted_parameters.append(params)

    def retrieve_values(self, ID):
        values = []
        for posterior in self._accepted_parameters :
            values.append([x.value(ID) for x in posterior])
        return values;

    def plot(self, fig):
        nb_figures = len(self._non_dirac_priors)
        assert(nb_figures >= 1), "There are no non_dirac prior in the model"
        y = 1
        x = math.floor(nb_figures / y) + 1
        i = 0
        for ID in self._non_dirac_priors.keys():
            prior = self._non_dirac_priors[ID]
            absciss = prior.absciss_range()
            x_points = np.linspace(absciss.min - 1, absciss.max + 1, 10000)
            values = self.retrieve_values(ID)
            axes = fig.add_subplot(x, y, i+1)
            true_theta = self._true_param.value(ID)
            self.__plot_parameter(axes, x_points, values, true_theta, prior.pdf(), self._plot_names[ID])
            i += 1

        return fig;
