package analysis.api;

import analysis.dto.Response;
import analysis.functions.Matrix;
import analysis.functions.PrimeNumber;
import analysis.functions.Weather;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FunctionEndpoint {

    @GetMapping("prime-number")
    public Response primeNumber(@RequestParam(value = "num") Integer num) {
        return new Response(PrimeNumber.getNthPrimeNumber(num));
    }

    @GetMapping("matrix")
    public Response matrix(@RequestParam(value = "size") Integer size, @RequestParam(value = "ramLoader") Long ramLoader) {
        return new Response(Matrix.multiplyRandomMatrices(size, ramLoader));
    }

    @GetMapping("weather")
    public Response weather(@RequestParam(value = "location") String location) {
        return new Response(Weather.getWeather(location));
    }

}
