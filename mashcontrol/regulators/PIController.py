import time
class PIController:
    '''
    Discrete implementation of the PI controller with a feedforward input
    Windup is avoided as the feedback is limited over both the Process and feedforward change
    '''
    
    def __init__(self, K=0.7, Tr=25.0, max_output=100, min_output= 0, maxTempChange=6.5):
        """ 
        @param K: Gain
        @param Tr: Reset time in repeats per minute
        @param max_output: The maximum output signal 
        @param min_output: The minimum output signal
        """
        self.K = K
        self.Tr = Tr

        self.max_output = max_output
        self.min_output = min_output

        self._dt = 0.0
        self._feedback = 0.0
        self._last_feedforward = 0.0
        self.running = False

        self.targetTemperature = 0
        self._maxTempChange = maxTempChange

    def _limit_output(self, control_value):
        # Signal limitation
        control_value = min(control_value, self.max_output)
        control_value = max(control_value, self.min_output)
        return control_value

    def get_error(self, outTemp):
        return self.targetTemperature - outTemp

    def get_feedforward(self, inTemp):
        if inTemp is None:
            return 0
        return ((self.targetTemperature - inTemp)/self._maxTempChange)*100

    def get_control_value(self, inTemp, outTemp):
        """
        @summary: Updating the PID controller parameters
        
        @param error: The error between the predefined value and the measured value
        @param feedforward: The Calculated outputvalue from the feedforward control
        
        @return: The control signal  
        """
        
        error = self.get_error(outTemp)
        feedforward = self.get_feedforward(inTemp)
        
        if not self.running:
            self.feedback = feedforward
            return

        now = time.time()
        
        if not self._dt: #Initial run
            output = self._limit_output(feedforward)
            feedback = output
            self._last_feedforward = feedforward

        else:
            #Change in output is the gain + the change in feedforward value
            change = (error * self.K) + (feedforward - self._last_feedforward)
        
            output = change + self._feedback
            output = self._limit_output(output)

            dt = now - self._dt
            
            integral_weight = (self.Tr/60)*dt
            
            #Since the feedforward change will only be recorded in the feedback for the integral weight,
            #    make sure the last_feedforwad is only affected by the same portion
            self._last_feedforward = self._last_feedforward +integral_weight*(feedforward-self._last_feedforward)

            feedback=self._feedback+(output-self._feedback)*integral_weight
            
        
        # Storing the time
        self._dt = now
            
        self._feedback = feedback
        
        return output
    
    def start(self):
        self._dt = None
        self._last_feedforward = 0
        self.running = True

    def stop(self):
        self.running = False