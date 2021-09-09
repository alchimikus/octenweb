import { createGlobalStyle} from "styled-components"
const GlobalStyles = createGlobalStyle`
   * {
    background-color: ${({ theme }) => theme.body};
    color: ${({ theme }) => theme.text};
    font-family: Tahoma, Helvetica, Arial, Roboto, sans-serif;
    transition: all 0.50s linear;
     
  }
  
  
  
  `
export {GlobalStyles}