'''
Defines a class, Neuron473834758, of neurons from Allen Brain Institute's model 473834758

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473834758:
    def __init__(self, name="Neuron473834758", x=0, y=0, z=0):
        '''Instantiate Neuron473834758.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473834758_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Nr5a1-Cre_Ai14_IVSCC_-172512.05.01.01_466657408_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473834758_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 28.36
            sec.e_pas = -96.3921763102
        for sec in self.apic:
            sec.cm = 4.72
            sec.g_pas = 0.000238868927739
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000294059603637
        for sec in self.dend:
            sec.cm = 4.72
            sec.g_pas = 1e-07
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.00123546
            sec.gbar_Ih = 3.95887e-06
            sec.gbar_NaTs = 0.652524
            sec.gbar_Nap = 0.000264353
            sec.gbar_K_P = 0.0392481
            sec.gbar_K_T = 0.00394172
            sec.gbar_SK = 0.000282822
            sec.gbar_Kv3_1 = 0.216112
            sec.gbar_Ca_HVA = 0.000286292
            sec.gbar_Ca_LVA = 0.00326074
            sec.gamma_CaDynamics = 0.00386732
            sec.decay_CaDynamics = 569.563
            sec.g_pas = 0.00023543
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

