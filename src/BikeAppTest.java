import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class BikeAppTest {
@Test
    public void TestThatBikeReturnsTrueValue() {
        BikeApp bikeApp = new BikeApp();
        bikeApp.setisPower(true);
        bikeApp.setSpeed(68);

        assertTrue(bikeApp.getisPower()==true);
    }
@Test
    public void TestThatBikeSwitchesOn(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(false);
    bikeApp.powerOn();

    assertTrue(bikeApp.getisPower()==true);
}
@Test
    public void TestThatBikeSwitchesOff(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.powerOff();

    assertTrue(bikeApp.getisPower()==false);
}
@Test
    public void TestThatTheGearOneAccelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(7);
    bikeApp.accelerateGearOne();

    assertEquals(8, bikeApp.getSpeed());
}
@Test
    public void TestThatTheGearTwoAccelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(21);
    bikeApp.accelerateGearTwo();

    assertEquals(23, bikeApp.getSpeed());
}
@Test
    public void TestThatTheGearThreeAccelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(31);
    bikeApp.accelerateGearThree();

    assertEquals(34, bikeApp.getSpeed());
}
@Test
    public void TestThatTheGearFourAccelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(43);
    bikeApp.accelerateGearFour();

    assertEquals(47, bikeApp.getSpeed());
}
@Test
    public void TestThatTheGearOneDecelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(2);
    bikeApp.decelerateGearOne();

    assertEquals(1, bikeApp.getSpeed());
}
@Test
    public void TestThatTheGearTwoDecelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(21);
    bikeApp.decelerateGearTwo();

    assertEquals(19, bikeApp.getSpeed());
}
@Test
    public void TestThatTheGearThreeDecelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(31);
    bikeApp.decelerateGearThree();

    assertEquals(28, bikeApp.getSpeed());
}
@Test
    public void TestThatTheGearFourDecelerates(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(true);
    bikeApp.setSpeed(43);
    bikeApp.decelerateGearFour();

    assertEquals(39, bikeApp.getSpeed());
}
@Test
    public void TestThatNoOperationIsALlowedWhenTheBikeIsOff(){
    BikeApp bikeApp = new BikeApp();
    bikeApp.setisPower(false);
    bikeApp.setSpeed(33);
    bikeApp.accelerateGearOne();

    assertEquals(0,bikeApp.getSpeed());
    }
}