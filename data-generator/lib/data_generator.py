'''
Copyright (c) 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
This source code is subject to the terms found in the AWS Enterprise Customer Agreement.
 '''

'''
 * Generates data based on a "shape" as defined by the following
 * <table border=1>
 * <caption>Data Shapes</caption>
 * <tr><th>Shape</th><th>Description</th><th>Implemented</th></tr>
 * <tr><td> jitter</td><td>[The default] Follows a single line with only slight variations bound by the min/max values in the json</td><td style="text-align:center">Y</td></tr>
 * <tr><td> rampup</td><td>Increments from min to max then resets to min </td><td style="text-align:center">N</td></tr>
 * <tr><td> rampdown</td><td>Decrements from max to min then resets to max </td><td style="text-align:center">N</td></tr>
 * <tr><td> triangle</td><td>Increments to max then decrements to min</td><td style="text-align:center">N</td></tr>
 * <tr><td> sinewave</td><td>Follows a sinusoidal value centered on (max-min)/2</td><td style="text-align:center">N</td></tr>
 * <tr><td> pwm50pc</td><td>Follows square wave shape with a 50 percent on duty cycle over 100 samples</td><td style="text-align:center">N</td></tr>
 * <tr><td> pwm25pd</td><td>Follows square wave shape with a 25 percent on duty cycle over 100 samples </td><td style="text-align:center">N</td></tr>
 * <tr><td> pwm75pc</td><td>Follows square wave shape with a 75 percent on duty cycle over 100 samples </td><td style="text-align:center">N</td></tr>
 * </table>
 * @author greenzcg
'''

from enum import Enum
import random

class shapes(Enum):
    JITTER = 1
    RAMPUP = 2
    RAMPDOWN = 3
    TRIANGLE = 4
    SINEWAVE = 5
    PWM25PC = 6
    PWM50PC = 7
    PWM75PC = 8

class DataGenerator:

    triangle_up = True
    pwm25_count = 0
    pwm50_count = 0
    pwm75_count = 0

    '''
     * Constructor
    '''
    def __init__(self):
        pass

    '''
     * Calculate the next value based on the parameters provided.
     * @param last
     * @param shape
     * @param max
     * @param min
     * @return
     '''
    def nextValueFrom(self, last, max_delta, shape, max, min):
        next = 0

        if shape == shapes.JITTER:
            next = last + (random.random() * max_delta - max_delta/2)
            if next > max: next = max
            if next < min: next = min

        elif shape == shapes.RAMPUP:
            next = last + 1
            if next > max: next = min
            if next < min: next = min

        elif shape == shapes.RAMPDOWN:
            next = last - 1
            if next < min: next = max
            if next > max: next = max

        elif shape == shapes.TRIANGLE:
            if self.triangle_up == True:
                # increment
                next = last + 1
                if next > max:
                    next = max - 1
                    self.triangle_up = False
            else:
                # decrement
                next = last - 1
                if next < min:
                    next = min + 1
                    self.triangle_up = True

        elif shape == shapes.SINEWAVE:
            pass

        elif shape == shapes.PWM25PC:
            self.pwm25_count += 1
            if self.pwm25_count > max:
                self.pwm25_count = 0
            if self.pwm25_count > max * 0.25:
                next = 0
            else:
                next = 1

        elif shape == shapes.PWM50PC:
            self.pwm50_count += 1
            if self.pwm50_count > max:
                self.pwm50_count = 0
            if self.pwm50_count > max * 0.5:
                next = 0
            else:
                next = 1

        elif shape == shapes.PWM75PC:
            self.pwm75_count += 1
            if self.pwm75_count > max:
                self.pwm75_count = 0
            if self.pwm75_count > max * 0.75:
                next = 0
            else:
                next = 1

        return next

if __name__ == "__main__":
    print("This is just a test")
    dg = DataGenerator()
    next = 0
    for x in range(0,40):
        next = dg.nextValueFrom(next, 5, shapes.RAMPDOWN, 10, 0)
        print("The next value is " + str(next))
