import unittest

import Parser
import model

class TestCrossValidation(unittest.TestCase):

    def test(self):

        import json

        m = { 'prior' : [
                                    {
                                    'name' : 'mu',
                                    'distribution' : {
                                        'name' : 'dirac',
                                        'param' : [
                                            {
                                            'name' : 'd',
                                            'value' : 0,
                                            }
                                        ]
                                        }
                                    },
                                    {
                                    'name' : 'sigma',
                                    'distribution' : {
                                        'name' : 'dirac',
                                        'param' : [
                                            {
                                            'name' : 'd',
                                            'value' : 1000,
                                            }
                                        ]
                                        }
                                    },
                                    {
                                    'name' : 'r',
                                    'distribution' : {
                                        'name' : 'dirac',
                                        'param' : [
                                            {
                                            'name' : 'd',
                                            'value' : 2,
                                            }
                                        ]
                                        }
                                    },
                                    {
                                    'name' : 'k',
                                    'distribution' : {
                                        'name' : 'uniform_int',
                                        'param' : [
                                            {
                                            'name' : 'a',
                                            'value' : 1,
                                            },
                                            {
                                            'name' : 'b',
                                            'value' : 100,
                                            }
                                        ]
                                        }
                                    }
                              ],
                'posteriors' : {
                    1 : [
                            {
                            'mu' : 0,
                            'sigma' : 1000,
                            'r' : 2,
                            'k' : 5
                            },
                            {
                            'mu' : 0,
                            'sigma' : 1000,
                            'r' : 2,
                            'k' : 50
                            }
                        ],
                    2 : [
                            {
                            'mu' : 0,
                            'sigma' : 1000,
                            'r' : 2,
                            'k' : 75
                            },
                            {
                            'mu' : 0,
                            'sigma' : 1000,
                            'r' : 2,
                            'k' : 34
                            }
                    ]
                }
        }


        import matplotlib.pyplot as plt

        make = lambda w, x, y, z : model.Param(['mu','sigma', 'r', 'k'], [w,x,y,z])
        true_theta = make(0, 1000, 2, 50)

        unif_k = model.Uniform(1,100)
        plot_names = {'mu':'$\mu$', 'sigma':'$\sigma$', 'r':'r', 'k':'K'}

        parser = Parser.Parser()
        cv = parser.build_cross_validation(m['posteriors'], {'k' : unif_k} , true_theta , plot_names)

        #cv = graphics.CrossValidation( {'K' : unif_k} , true_theta , plot_names)

        fig = plt.figure()
        fig = cv.plot(fig)
        plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.75, wspace=0.35)
        plt.show()



if __name__ == '__main__':
    unittest.main()
