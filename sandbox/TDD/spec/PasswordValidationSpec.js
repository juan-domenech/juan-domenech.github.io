//Kata: Password Validation
//Problem Description
//Create a function passwordValidation() that receives a string and returns true when:
//the string contains at least one letter in uppercase
//the string contains at least 2 numbers (digits)
//the string contains at least one of these special characters: $ # % & - ! ?
//the string has 10 characters or more
//Otherwise the function should return true


  describe("A function PasswordValidation()", function() {
    it("should be defined", function() {
        expect( PasswordValidation ).toBeDefined();
      });

    it("should accept one parameter", function() {
      expect( PasswordValidation.length ).toEqual(1);
    });

    it("should return 'false' when no parameter is passed", function() {
      expect( PasswordValidation() ).toEqual(false);
    });

    it("should return 'false' when there is no letter in uppercase", function() {
      expect( PasswordValidation('abc1defg2hijk!') ).toEqual(false);
    });

    it("should return 'true' when there is a letter in uppercase", function() {
      expect( PasswordValidation('Abc1defg2hijk!') ).toEqual(true);
    });

    it("should return 'true' when there are 2 or more numbers", function() {
      expect( PasswordValidation('Abc1defg2hijk!') ).toEqual(true);
    });

    it("should return 'false' when password is less than 10 characters long", function() {
      expect( PasswordValidation('Abc1g2k!') ).toEqual(false);
    });

    it("should return 'true' when contains '!'", function() {
      expect( PasswordValidation('Abc1defg2hijk!') ).toEqual(true);
    });

    it("should return 'true' when contains '?'", function() {
      expect( PasswordValidation('Abc1defg2hijk?') ).toEqual(true);
    });

    it("should return 'true' when contains '$'", function() {
      expect( PasswordValidation('Abc1defg2hijk$') ).toEqual(true);
    });

    it("should return 'true' when contains '#'", function() {
      expect( PasswordValidation('Abc1defg2hijk#') ).toEqual(true);
    });

    it("should return 'true' when contains '%'", function() {
      expect( PasswordValidation('Abc1defg2hijk%') ).toEqual(true);
    });

    it("should return 'true' when contains '&'", function() {
      expect( PasswordValidation('Abc1defg2hijk&') ).toEqual(true);
    });

    it("should return 'true' when contains '-'", function() {
      expect( PasswordValidation('Abc1defg2hijk-') ).toEqual(true);
    });


  });