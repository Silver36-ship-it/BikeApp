public class BikeApp {
    private boolean isPower = false;
    private int speed;

    public boolean getisPower(){
        return isPower;
    }
    public void setisPower(boolean isPower) {
            this.isPower = isPower;
    }
    public int getSpeed(){
        if(!isPower){
            return 0;
        }
        return speed;
    }
    public void setSpeed(int speed){
        if (this.isPower && speed > 0) {
            this.speed = speed;
        }
    }
    public void powerOff(){
        isPower = false;
    }
    public void powerOn(){
        isPower = true;
    }

    public void accelerateGearOne(){
        if(isPower && speed > 0 && speed <= 20){
            speed += 1;
        }

    }
    public void accelerateGearTwo(){
        if(isPower && speed > 20 && speed <= 30){
            speed += 2;
        }
    }
    public void accelerateGearThree(){
        if(isPower && speed > 30 && speed <= 40){
            speed += 3;
        }
    }
    public void accelerateGearFour(){
        if(isPower && speed > 40){
            speed += 4;
        }
    }
    public void decelerateGearOne(){
        if(isPower && speed > 0 && speed <= 20){
            speed -= 1;
        }
    }
    public void decelerateGearTwo(){
        if(isPower && speed > 20 && speed <= 30){
            speed -= 2;
        }
    }
    public void decelerateGearThree(){
        if(isPower && speed > 30 && speed <= 40){
            speed -= 3;
        }
    }
    public void decelerateGearFour(){
        if(isPower && speed > 40){
            speed -= 4;
        }
    }
}